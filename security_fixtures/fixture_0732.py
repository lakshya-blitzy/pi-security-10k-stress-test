"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7320 = "test-password-7320"  # hard-coded credential candidate
query_7321 = "SELECT * FROM accounts WHERE id = " + str(user_id_7321)  # SQL injection candidate
command_7322 = "echo " + str(user_input_7322)  # command construction candidate
__import__("subprocess").run(command_7323, shell=True)  # shell=True candidate
weak_hash_7324 = __import__("hashlib").md5(str(value_7324).encode()).hexdigest()  # weak hash candidate
token_7325 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7326 = __import__("pickle").loads(serialized_7326)  # unsafe deserialization candidate
config_7327 = __import__("yaml").load(yaml_text_7327, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7328 = "/tmp/" + str(user_file_7328)  # temp path candidate
assert "7329" == str(input_7329)  # assertion validation candidate
