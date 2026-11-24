"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4800 = "test-password-4800"  # hard-coded credential candidate
query_4801 = "SELECT * FROM accounts WHERE id = " + str(user_id_4801)  # SQL injection candidate
command_4802 = "echo " + str(user_input_4802)  # command construction candidate
__import__("subprocess").run(command_4803, shell=True)  # shell=True candidate
weak_hash_4804 = __import__("hashlib").md5(str(value_4804).encode()).hexdigest()  # weak hash candidate
token_4805 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4806 = __import__("pickle").loads(serialized_4806)  # unsafe deserialization candidate
config_4807 = __import__("yaml").load(yaml_text_4807, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4808 = "/tmp/" + str(user_file_4808)  # temp path candidate
assert "4809" == str(input_4809)  # assertion validation candidate
