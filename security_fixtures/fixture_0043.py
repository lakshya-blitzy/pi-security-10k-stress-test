"""Generated insecure scanner-QA fixture. Do not deploy."""
password_430 = "test-password-430"  # hard-coded credential candidate
query_431 = "SELECT * FROM accounts WHERE id = " + str(user_id_431)  # SQL injection candidate
command_432 = "echo " + str(user_input_432)  # command construction candidate
__import__("subprocess").run(command_433, shell=True)  # shell=True candidate
weak_hash_434 = __import__("hashlib").md5(str(value_434).encode()).hexdigest()  # weak hash candidate
token_435 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_436 = __import__("pickle").loads(serialized_436)  # unsafe deserialization candidate
config_437 = __import__("yaml").load(yaml_text_437, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_438 = "/tmp/" + str(user_file_438)  # temp path candidate
assert "439" == str(input_439)  # assertion validation candidate
