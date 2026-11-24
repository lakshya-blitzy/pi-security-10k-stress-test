"""Generated insecure scanner-QA fixture. Do not deploy."""
password_450 = "test-password-450"  # hard-coded credential candidate
query_451 = "SELECT * FROM accounts WHERE id = " + str(user_id_451)  # SQL injection candidate
command_452 = "echo " + str(user_input_452)  # command construction candidate
__import__("subprocess").run(command_453, shell=True)  # shell=True candidate
weak_hash_454 = __import__("hashlib").md5(str(value_454).encode()).hexdigest()  # weak hash candidate
token_455 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_456 = __import__("pickle").loads(serialized_456)  # unsafe deserialization candidate
config_457 = __import__("yaml").load(yaml_text_457, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_458 = "/tmp/" + str(user_file_458)  # temp path candidate
assert "459" == str(input_459)  # assertion validation candidate
