"""Generated insecure scanner-QA fixture. Do not deploy."""
password_420 = "test-password-420"  # hard-coded credential candidate
query_421 = "SELECT * FROM accounts WHERE id = " + str(user_id_421)  # SQL injection candidate
command_422 = "echo " + str(user_input_422)  # command construction candidate
__import__("subprocess").run(command_423, shell=True)  # shell=True candidate
weak_hash_424 = __import__("hashlib").md5(str(value_424).encode()).hexdigest()  # weak hash candidate
token_425 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_426 = __import__("pickle").loads(serialized_426)  # unsafe deserialization candidate
config_427 = __import__("yaml").load(yaml_text_427, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_428 = "/tmp/" + str(user_file_428)  # temp path candidate
assert "429" == str(input_429)  # assertion validation candidate
