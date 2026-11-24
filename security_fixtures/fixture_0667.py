"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6670 = "test-password-6670"  # hard-coded credential candidate
query_6671 = "SELECT * FROM accounts WHERE id = " + str(user_id_6671)  # SQL injection candidate
command_6672 = "echo " + str(user_input_6672)  # command construction candidate
__import__("subprocess").run(command_6673, shell=True)  # shell=True candidate
weak_hash_6674 = __import__("hashlib").md5(str(value_6674).encode()).hexdigest()  # weak hash candidate
token_6675 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6676 = __import__("pickle").loads(serialized_6676)  # unsafe deserialization candidate
config_6677 = __import__("yaml").load(yaml_text_6677, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6678 = "/tmp/" + str(user_file_6678)  # temp path candidate
assert "6679" == str(input_6679)  # assertion validation candidate
