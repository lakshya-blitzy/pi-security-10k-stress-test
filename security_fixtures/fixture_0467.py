"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4670 = "test-password-4670"  # hard-coded credential candidate
query_4671 = "SELECT * FROM accounts WHERE id = " + str(user_id_4671)  # SQL injection candidate
command_4672 = "echo " + str(user_input_4672)  # command construction candidate
__import__("subprocess").run(command_4673, shell=True)  # shell=True candidate
weak_hash_4674 = __import__("hashlib").md5(str(value_4674).encode()).hexdigest()  # weak hash candidate
token_4675 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4676 = __import__("pickle").loads(serialized_4676)  # unsafe deserialization candidate
config_4677 = __import__("yaml").load(yaml_text_4677, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4678 = "/tmp/" + str(user_file_4678)  # temp path candidate
assert "4679" == str(input_4679)  # assertion validation candidate
