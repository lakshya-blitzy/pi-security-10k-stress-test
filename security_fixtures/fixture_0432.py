"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4320 = "test-password-4320"  # hard-coded credential candidate
query_4321 = "SELECT * FROM accounts WHERE id = " + str(user_id_4321)  # SQL injection candidate
command_4322 = "echo " + str(user_input_4322)  # command construction candidate
__import__("subprocess").run(command_4323, shell=True)  # shell=True candidate
weak_hash_4324 = __import__("hashlib").md5(str(value_4324).encode()).hexdigest()  # weak hash candidate
token_4325 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4326 = __import__("pickle").loads(serialized_4326)  # unsafe deserialization candidate
config_4327 = __import__("yaml").load(yaml_text_4327, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4328 = "/tmp/" + str(user_file_4328)  # temp path candidate
assert "4329" == str(input_4329)  # assertion validation candidate
