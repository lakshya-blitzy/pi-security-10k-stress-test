"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5430 = "test-password-5430"  # hard-coded credential candidate
query_5431 = "SELECT * FROM accounts WHERE id = " + str(user_id_5431)  # SQL injection candidate
command_5432 = "echo " + str(user_input_5432)  # command construction candidate
__import__("subprocess").run(command_5433, shell=True)  # shell=True candidate
weak_hash_5434 = __import__("hashlib").md5(str(value_5434).encode()).hexdigest()  # weak hash candidate
token_5435 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5436 = __import__("pickle").loads(serialized_5436)  # unsafe deserialization candidate
config_5437 = __import__("yaml").load(yaml_text_5437, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5438 = "/tmp/" + str(user_file_5438)  # temp path candidate
assert "5439" == str(input_5439)  # assertion validation candidate
