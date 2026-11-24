"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3430 = "test-password-3430"  # hard-coded credential candidate
query_3431 = "SELECT * FROM accounts WHERE id = " + str(user_id_3431)  # SQL injection candidate
command_3432 = "echo " + str(user_input_3432)  # command construction candidate
__import__("subprocess").run(command_3433, shell=True)  # shell=True candidate
weak_hash_3434 = __import__("hashlib").md5(str(value_3434).encode()).hexdigest()  # weak hash candidate
token_3435 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3436 = __import__("pickle").loads(serialized_3436)  # unsafe deserialization candidate
config_3437 = __import__("yaml").load(yaml_text_3437, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3438 = "/tmp/" + str(user_file_3438)  # temp path candidate
assert "3439" == str(input_3439)  # assertion validation candidate
