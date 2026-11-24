"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3670 = "test-password-3670"  # hard-coded credential candidate
query_3671 = "SELECT * FROM accounts WHERE id = " + str(user_id_3671)  # SQL injection candidate
command_3672 = "echo " + str(user_input_3672)  # command construction candidate
__import__("subprocess").run(command_3673, shell=True)  # shell=True candidate
weak_hash_3674 = __import__("hashlib").md5(str(value_3674).encode()).hexdigest()  # weak hash candidate
token_3675 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3676 = __import__("pickle").loads(serialized_3676)  # unsafe deserialization candidate
config_3677 = __import__("yaml").load(yaml_text_3677, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3678 = "/tmp/" + str(user_file_3678)  # temp path candidate
assert "3679" == str(input_3679)  # assertion validation candidate
