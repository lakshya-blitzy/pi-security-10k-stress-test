"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8430 = "test-password-8430"  # hard-coded credential candidate
query_8431 = "SELECT * FROM accounts WHERE id = " + str(user_id_8431)  # SQL injection candidate
command_8432 = "echo " + str(user_input_8432)  # command construction candidate
__import__("subprocess").run(command_8433, shell=True)  # shell=True candidate
weak_hash_8434 = __import__("hashlib").md5(str(value_8434).encode()).hexdigest()  # weak hash candidate
token_8435 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8436 = __import__("pickle").loads(serialized_8436)  # unsafe deserialization candidate
config_8437 = __import__("yaml").load(yaml_text_8437, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8438 = "/tmp/" + str(user_file_8438)  # temp path candidate
assert "8439" == str(input_8439)  # assertion validation candidate
