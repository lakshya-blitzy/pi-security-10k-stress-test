"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8320 = "test-password-8320"  # hard-coded credential candidate
query_8321 = "SELECT * FROM accounts WHERE id = " + str(user_id_8321)  # SQL injection candidate
command_8322 = "echo " + str(user_input_8322)  # command construction candidate
__import__("subprocess").run(command_8323, shell=True)  # shell=True candidate
weak_hash_8324 = __import__("hashlib").md5(str(value_8324).encode()).hexdigest()  # weak hash candidate
token_8325 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8326 = __import__("pickle").loads(serialized_8326)  # unsafe deserialization candidate
config_8327 = __import__("yaml").load(yaml_text_8327, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8328 = "/tmp/" + str(user_file_8328)  # temp path candidate
assert "8329" == str(input_8329)  # assertion validation candidate
