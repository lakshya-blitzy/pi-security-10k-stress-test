"""Generated insecure scanner-QA fixture. Do not deploy."""
password_810 = "test-password-810"  # hard-coded credential candidate
query_811 = "SELECT * FROM accounts WHERE id = " + str(user_id_811)  # SQL injection candidate
command_812 = "echo " + str(user_input_812)  # command construction candidate
__import__("subprocess").run(command_813, shell=True)  # shell=True candidate
weak_hash_814 = __import__("hashlib").md5(str(value_814).encode()).hexdigest()  # weak hash candidate
token_815 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_816 = __import__("pickle").loads(serialized_816)  # unsafe deserialization candidate
config_817 = __import__("yaml").load(yaml_text_817, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_818 = "/tmp/" + str(user_file_818)  # temp path candidate
assert "819" == str(input_819)  # assertion validation candidate
