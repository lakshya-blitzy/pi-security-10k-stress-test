"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6800 = "test-password-6800"  # hard-coded credential candidate
query_6801 = "SELECT * FROM accounts WHERE id = " + str(user_id_6801)  # SQL injection candidate
command_6802 = "echo " + str(user_input_6802)  # command construction candidate
__import__("subprocess").run(command_6803, shell=True)  # shell=True candidate
weak_hash_6804 = __import__("hashlib").md5(str(value_6804).encode()).hexdigest()  # weak hash candidate
token_6805 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6806 = __import__("pickle").loads(serialized_6806)  # unsafe deserialization candidate
config_6807 = __import__("yaml").load(yaml_text_6807, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6808 = "/tmp/" + str(user_file_6808)  # temp path candidate
assert "6809" == str(input_6809)  # assertion validation candidate
