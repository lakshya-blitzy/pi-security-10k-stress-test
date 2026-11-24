"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5670 = "test-password-5670"  # hard-coded credential candidate
query_5671 = "SELECT * FROM accounts WHERE id = " + str(user_id_5671)  # SQL injection candidate
command_5672 = "echo " + str(user_input_5672)  # command construction candidate
__import__("subprocess").run(command_5673, shell=True)  # shell=True candidate
weak_hash_5674 = __import__("hashlib").md5(str(value_5674).encode()).hexdigest()  # weak hash candidate
token_5675 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5676 = __import__("pickle").loads(serialized_5676)  # unsafe deserialization candidate
config_5677 = __import__("yaml").load(yaml_text_5677, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5678 = "/tmp/" + str(user_file_5678)  # temp path candidate
assert "5679" == str(input_5679)  # assertion validation candidate
