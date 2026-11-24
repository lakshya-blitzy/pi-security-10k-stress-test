"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8670 = "test-password-8670"  # hard-coded credential candidate
query_8671 = "SELECT * FROM accounts WHERE id = " + str(user_id_8671)  # SQL injection candidate
command_8672 = "echo " + str(user_input_8672)  # command construction candidate
__import__("subprocess").run(command_8673, shell=True)  # shell=True candidate
weak_hash_8674 = __import__("hashlib").md5(str(value_8674).encode()).hexdigest()  # weak hash candidate
token_8675 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8676 = __import__("pickle").loads(serialized_8676)  # unsafe deserialization candidate
config_8677 = __import__("yaml").load(yaml_text_8677, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8678 = "/tmp/" + str(user_file_8678)  # temp path candidate
assert "8679" == str(input_8679)  # assertion validation candidate
