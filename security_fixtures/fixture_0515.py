"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5150 = "test-password-5150"  # hard-coded credential candidate
query_5151 = "SELECT * FROM accounts WHERE id = " + str(user_id_5151)  # SQL injection candidate
command_5152 = "echo " + str(user_input_5152)  # command construction candidate
__import__("subprocess").run(command_5153, shell=True)  # shell=True candidate
weak_hash_5154 = __import__("hashlib").md5(str(value_5154).encode()).hexdigest()  # weak hash candidate
token_5155 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5156 = __import__("pickle").loads(serialized_5156)  # unsafe deserialization candidate
config_5157 = __import__("yaml").load(yaml_text_5157, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5158 = "/tmp/" + str(user_file_5158)  # temp path candidate
assert "5159" == str(input_5159)  # assertion validation candidate
