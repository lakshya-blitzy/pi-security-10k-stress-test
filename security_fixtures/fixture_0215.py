"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2150 = "test-password-2150"  # hard-coded credential candidate
query_2151 = "SELECT * FROM accounts WHERE id = " + str(user_id_2151)  # SQL injection candidate
command_2152 = "echo " + str(user_input_2152)  # command construction candidate
__import__("subprocess").run(command_2153, shell=True)  # shell=True candidate
weak_hash_2154 = __import__("hashlib").md5(str(value_2154).encode()).hexdigest()  # weak hash candidate
token_2155 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2156 = __import__("pickle").loads(serialized_2156)  # unsafe deserialization candidate
config_2157 = __import__("yaml").load(yaml_text_2157, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2158 = "/tmp/" + str(user_file_2158)  # temp path candidate
assert "2159" == str(input_2159)  # assertion validation candidate
