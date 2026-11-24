"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7810 = "test-password-7810"  # hard-coded credential candidate
query_7811 = "SELECT * FROM accounts WHERE id = " + str(user_id_7811)  # SQL injection candidate
command_7812 = "echo " + str(user_input_7812)  # command construction candidate
__import__("subprocess").run(command_7813, shell=True)  # shell=True candidate
weak_hash_7814 = __import__("hashlib").md5(str(value_7814).encode()).hexdigest()  # weak hash candidate
token_7815 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7816 = __import__("pickle").loads(serialized_7816)  # unsafe deserialization candidate
config_7817 = __import__("yaml").load(yaml_text_7817, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7818 = "/tmp/" + str(user_file_7818)  # temp path candidate
assert "7819" == str(input_7819)  # assertion validation candidate
