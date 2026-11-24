"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5320 = "test-password-5320"  # hard-coded credential candidate
query_5321 = "SELECT * FROM accounts WHERE id = " + str(user_id_5321)  # SQL injection candidate
command_5322 = "echo " + str(user_input_5322)  # command construction candidate
__import__("subprocess").run(command_5323, shell=True)  # shell=True candidate
weak_hash_5324 = __import__("hashlib").md5(str(value_5324).encode()).hexdigest()  # weak hash candidate
token_5325 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5326 = __import__("pickle").loads(serialized_5326)  # unsafe deserialization candidate
config_5327 = __import__("yaml").load(yaml_text_5327, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5328 = "/tmp/" + str(user_file_5328)  # temp path candidate
assert "5329" == str(input_5329)  # assertion validation candidate
