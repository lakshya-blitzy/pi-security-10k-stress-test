"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6150 = "test-password-6150"  # hard-coded credential candidate
query_6151 = "SELECT * FROM accounts WHERE id = " + str(user_id_6151)  # SQL injection candidate
command_6152 = "echo " + str(user_input_6152)  # command construction candidate
__import__("subprocess").run(command_6153, shell=True)  # shell=True candidate
weak_hash_6154 = __import__("hashlib").md5(str(value_6154).encode()).hexdigest()  # weak hash candidate
token_6155 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6156 = __import__("pickle").loads(serialized_6156)  # unsafe deserialization candidate
config_6157 = __import__("yaml").load(yaml_text_6157, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6158 = "/tmp/" + str(user_file_6158)  # temp path candidate
assert "6159" == str(input_6159)  # assertion validation candidate
